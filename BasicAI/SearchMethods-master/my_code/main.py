from bfs import bfs_paths
from dfs import dfs_paths

from dict import cities_and_paths
from iterative import iterative_path

src = input('Enter the source:\n')
dst = input('Enter the destination:\n')
while src not in cities_and_paths or dst not in cities_and_paths:
    print('No such city name')
    src = input('Enter correct source city:\n')
    dst = input('Enter correct destination city:\n')

method = input('Enter the type of search you want to:\n(give input as bfs or dfs or iterative)\n')
method = method.lower()
while method != 'bfs' or method != 'dfs' or method != 'iterative':
    method = input('Enter the correct method:\n')
if method == 'bfs':
    bfs_paths(src, dst)
elif method == 'dfs':
    dfs_paths(src, dst)
elif method == 'iterative':
    iterative_path(src, dst)
