def towerhanoi(n,source,spare,target):
    if n==1:
        print(f'move disk from {source} to {target}')
        return
    else:
        towerhanoi(n-1,source,target,spare)
        towerhanoi(1,source,spare,target)
        towerhanoi(n-1,spare,source,target)
towerhanoi(3,'s','l','d')
