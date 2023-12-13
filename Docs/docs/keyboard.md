# Keyboard

![](board-keyboard.png)
![](keyboard.png)

The KITTY uses a custom 40-key mechanical keyboard for input, which is connected to the main board via two cables.

The keyboard can be read directly by the cpu through means of 5 Keyboard Row Registers, where each bit in the byte represents the current state of a particular key (**0**=unpressed **1**=pressed).

| Address | Mode |  Description   | Format (bit 7-0)|
|---------|------|----------------|----------------------------------|
| `$7000` |  R   | Keyboard Row 1 | `O` `I` `U` `T` `R` `E` `W` `Esc`|
| `$7010` |  R   | Keyboard Row 2 | `P` `K` `J` `Y` `G` `S` `Q` `Alt`|
| `$7020` |  R   | Keyboard Row 3 | `Backspace` `L` `M` `H` `V` `D` `A` `Shift`|
| `$7030` |  R   | Keyboard Row 4 | `Enter` `.` `|` `N` `B` `F` `Z` `Menu` |
| `$7040` |  R   | Keyboard Row 5 | `→` `↓` `←` `↑` `Space` `C` `X` `Ctrl`|