#!/usr/bin/env python3
"""
qmd索引集成 - qmd-index-update.py
功能：调用qmd skill增量索引evidence/目录下的md文件，建立语义检索层
使用：python qmd-index-update.py --project-path "<项目路径>" [--full-rebuild]
设计：qmd索引是影子层，可从evidence/重建
注意：qmd embedding耗时问题已解决，可正常使用
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

# Windows PowerShell GBK编码修复：强制stdout用UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def find_qmd_binary():
    """查找qmd可执行文件"""
    # 尝试常见路径
    candidates = [
        Path(os.environ.get('HOME', '')) / '.cargo' / 'bin' / 'qmd.exe',
        Path(os.environ.get('USERPROFILE', '')) / '.cargo' / 'bin' / 'qmd.exe',
        Path('qmd.exe'),
    ]
    for c in candidates:
        if c.exists():
            return str(c)
    return 'qmd'  # 依赖PATH

def init_qmd_index(qmd_bin, index_path, evidence_path):
    """初始化qmd索引"""
    os.makedirs(index_path, exist_ok=True)

    # qmd init
    cmd = [qmd_bin, 'init', '--path', str(index_path)]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(f"  qmd init 失败: {result.stderr}")
        return False
    print(f"  qmd索引初始化: {index_path}")
    return True

def index_files(qmd_bin, index_path, files):
    """索引文件列表"""
    if not files:
        print("  无新文件需要索引")
        return 0

    indexed = 0
    for f in files:
        cmd = [qmd_bin, 'add', '--path', str(index_path), str(f)]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            if result.returncode == 0:
                indexed += 1
            else:
                print(f"  索引失败 {f.name}: {result.stderr[:200]}")
        except subprocess.TimeoutExpired:
            print(f"  索引超时 {f.name}")
        except Exception as e:
            print(f"  索引异常 {f.name}: {e}")

    return indexed

def get_existing_indexed_files(index_path):
    """获取已索引的文件列表（用于增量）"""
    manifest = index_path / 'manifest.json'
    if not manifest.exists():
        return set()

    import json
    try:
        with open(manifest, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return set(data.get('indexed_files', []))
    except:
        return set()

def main():
    parser = argparse.ArgumentParser(description='qmd索引集成')
    parser.add_argument('--project-path', required=True, help='项目路径')
    parser.add_argument('--full-rebuild', action='store_true', help='全量重建')
    args = parser.parse_args()

    pack_path = Path(args.project_path) / 'knowledge-pack'
    evidence_path = pack_path / 'evidence'
    qmd_index_path = pack_path / 'index' / 'qmd-index'

    if not evidence_path.exists():
        print(f"evidence目录不存在: {evidence_path}")
        return

    qmd_bin = find_qmd_binary()
    print(f"使用qmd: {qmd_bin}")

    # 收集所有md文件
    all_files = list(evidence_path.glob('*.md'))
    print(f"evidence目录共 {len(all_files)} 个md文件")

    if args.full_rebuild or not (qmd_index_path / 'manifest.json').exists():
        # 全量重建
        if qmd_index_path.exists():
            import shutil
            shutil.rmtree(qmd_index_path)
        if not init_qmd_index(qmd_bin, qmd_index_path, evidence_path):
            print("qmd初始化失败，退出")
            return
        files_to_index = all_files
    else:
        # 增量：只索引新增文件
        existing = get_existing_indexed_files(qmd_index_path)
        files_to_index = [f for f in all_files if f.name not in existing]

    print(f"需要索引 {len(files_to_index)} 个文件")
    indexed_count = index_files(qmd_bin, qmd_index_path, files_to_index)
    print(f"成功索引 {indexed_count} 个文件")

    # 更新manifest
    import json
    manifest_path = qmd_index_path / 'manifest.json'
    manifest = {
        'indexed_files': [f.name for f in all_files],
        'index_path': str(qmd_index_path),
        'evidence_path': str(evidence_path),
        'last_update': str(datetime.now(timezone.utc).isoformat()) if 'datetime' in dir() else ''
    }
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"qmd索引更新完成: {qmd_index_path}")

if __name__ == '__main__':
    from datetime import datetime, timezone
    main()
