# Installations
```
oh-my-zsh
tmux dotfiles: https://github.com/gpakosz/.tmux
p10k
```


# Fixing nvidia display issue
1. `sudo pacman -S nvidia`
2. Boot into arch and edit `/etc/default/grub`
  Add kernel option to the line `GRUB_CMDLINE_LINUX`
  ```
    GRUB_CMDLINE_LINUX="nvidia-drm.modeset=1"
  ```
  Regenerate `/boot/grub/grub.cfg`:
  ```
    grub-mkconfig -o /boot/grub/grub.cfg
  ```
