**哎呀呀好尴尬啊，可能是注释的时候破坏了某些东西的缩进关系，因为GitHub action用的是yaml来充当脚本，而yaml对于缩进关系要求严格，稍有不慎就会出错，不过坏事是手机上的GitHubAPP对于yaml的错误不会给予任何提示，需要在网页版里面查看（我觉得APP唯一的好处就是不需要梯子就可以流畅访问）**
```
name: CI #action的脚本在储存库里面的.github/workflows/name.yml，name可以是任何你喜欢的名字
on: [push] #这是定义action的运行条件，这里指的是只要储存库有推送就执行工作流
jobs:  #意思是下面是运行的工作
  package: #工作名称
    runs-on: ubuntu-latest #action的运行器有三个系统可以选择，Ubuntu-latest/windows-latest/macos-latest
    container: fedora #这里指的是要求拉取一个Docker环境，并且在那个Docker环境里面运行工作流
    steps: #指的是下面是执行工作的步骤
    - name: package#- name代表每个步骤的名称
      run: | #如果步骤有多个命令就需要用“ |”
        dnf makecache#这里就是执行的命令
        dnf -y up
        sudo dnf in -y gzip git fastfetch
    - name: clone src
      run: |
        git clone https://github.com/lwh2008/ll-rh.git
        ls
    - name: demo
      run: |
        ls #有一点值得注意的是，每一个步骤的（name）所在的目录和上一个步骤并没有关联，每一个步骤开始执行的时候都会回到初始目录
        cd ll-rh
        bash indep.sh
    - name: info
      run: fastfetch #待会瞅瞅免费的运行器硬件规格？看文档貌似运行器是虚拟机而不是容器。
```
我可能是注释忘掉空格了。。。
**应该可以看出来大部分的块是steps里面的内容，比如说和`runs-on`对齐的，前面是4个空格，不过`run`应该是和上面`name`对齐，另外就是别忘了里面字符之间的空格不要遗漏（曾经栽过坑），然后就是run里面的命令应该是在`run`的基础上面多加俩空格（或者是可以记成对齐`run`的`n`）
然后就是提交并运行，不过网页版好处是可以实时查看输出，APP这样的方便。。。
一般情况下如果仓库里面有其他的代码的话不太建议直接在GitHub里面改，不然服务器或者是电脑提交并推送代码以后会报错（因为本地储存库同步的更改不是最新的），往往需要执行`git pull origin master --rebase`，但是可能会丢失你上一次的文件（同步的是上一次成功提交的文件）
如果是实在是懒可以像我一样单独开一个专门跑action的储存库嘻嘻（doge）
**GitHub定价是这样的↓
所有的公共储存库的action免费，不过硬件规格的标准版，个人仓库是每个月免费2000分钟运行时间
至于高级版账号对于action的不同就是支持性能更好的action，GPU型action以及可以给action分组和一段时间内分配静态IP等等**
**另外就是你可以看到action的工作流和步骤处于什么状态，不要盲目相信他的状态提示，他是通过命令的返回状态判定的，主要还是要自己看（就像我这种情况😰）**
