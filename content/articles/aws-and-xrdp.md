# AWS and xrdp

2021-09-04

I don't know who needs to know this but, but I ended up struggling with this for a while this evening — here are some notes on getting an Remote Desktop connection to a Linux EC2 instance on AWS using `xrdp`. [^1]

You must do the following things:

* Allow incoming connections on the RDP port (3389 — see [AWS docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html)).
* Install `xrdp` and everything with `apt`, etc.
* Configure the correct window manager to run. I did this by editing `~/.xsession` to look like this: 
  
  ```
  xsetroot -solid gray
  exec xfce4-session
  ```
  
  (Obviously I'm using [xfce](http://xfce.org)).

* I'm connecting from a Windows machine, so using [Remote Desktop Connection](https://www.microsoft.com/en-us/p/microsoft-remote-desktop/9wzdncrfj3ps).

  Oddly, the middle mouse button (three fingers) from the Windows machine didn't work, so I monitored X input using `xev`. The mouse click showed up as a keypress, which I just remapped in a script. `117` was the keycode I was seeing from `xev`.
  
    xkbset m  
    xkbset exp =m  
    xmodmap -e "keycode 117 = Pointer_Button2"

This is probably deserving of more details — if you see this and have feedback, [tweet at me](http://twitter.com/nanaze), I guess. I just want to get this down somewhere so it comes up in a web search.

[^1] For context, I want to do some hobby development on a Linux machine but we mostly have Windows and Chrome devices sitting around the house. I could reimage an old machine, set up dual-boot, run VirtualBox, use [WSL](https://docs.microsoft.com/en-us/windows/wsl) or [Crostini](https://chromeos.dev/en/linux), etc, but all of these options are kind of a pain. Rather, I'd like to just have a cloud instance I can connect to from anywhere (namely either the office or the couch) and just costs a few cents per hour.