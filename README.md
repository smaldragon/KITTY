# Computer

## Memory Map
Address  | Function | Size (Kb)
---------|----------|-----
**$0000-6FFF**    | Work Ram | 28Kb
**$6800-6BFF**    | Palette Memory | 1Kb
**$6C00-6FFF**    | Character Memory | 1Kb
**$7000-7FFF**    | IO       | 4Kb
**$8000-FFFF**    | Cartridge Space (controled by BANK Register) | 32Kb


## IO Registers

Address  | Function | Mode | Bits
---------|---|--------|-----|
**$7000**| Keyboard Row 1 | R | <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Space</kbd> <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Space</kbd> <kbd>Ctrl</kbd> <kbd>Ctrl</kbd>
**$7010**| Keyboard Row 2 | R | <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Space</kbd> <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Space</kbd> <kbd>Ctrl</kbd> <kbd>Ctrl</kbd>
**$7020**| Keyboard Row 3 | R | <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Space</kbd> <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Space</kbd> <kbd>Ctrl</kbd> <kbd>Ctrl</kbd>
**$7030**| Keyboard Row 4 | R | <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Space</kbd> <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Space</kbd> <kbd>Ctrl</kbd> <kbd>Ctrl</kbd>
**$7040**| Keyboard Row 5 | R | <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Space</kbd> <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Space</kbd> <kbd>Ctrl</kbd> <kbd>Ctrl</kbd>
**$70D0**| BANK (active cartridge (0/1) + active 32Kb Bank (0-127) | W | `C BBBBBBB`
**$70E0**| Square 1 Freq | R/W | `FFFFFFFF` *1
**$70E0**| Square 2 Freq | R/W | `FFFFFFFF` *1
**$70E0**| Square 3 Freq | R/W | `FFFFFFFF` *1
**$70E0**| Freq Control Word (write before setting channel frequency) | R/W | `SS WW MMM B` *1
**$70F0**| Square 1 Volume (Left/Right) | W | `LLLL RRRR`
**$70F1**| Square 2 Volume (Left/Right) | W | `LLLL RRRR`
**$70F2**| Square 3 Volume (Left/Right) | W | `LLLL RRRR`
**$70F3**| Noise Volume    (Left/Right) | W | `LLLL RRRR`

> *1 - 82c54 Registers
