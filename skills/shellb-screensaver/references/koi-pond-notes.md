# How a finished screensaver is organised (Koi Pond)

`Koi Pond` (github.com/ShellB-App/Shell-B-Screensavers, `screensavers/koi-pond`) is 600 lines that follow one shape:

1. **A `CFG` block at the top**: water colours, moon position and size, koi count and speeds, ripple limits, lily pad
   count, the reduced-motion factor. Everything a reviewer might want to tune is there and nowhere else.
2. **Setup once**: canvas sized to the window with `devicePixelRatio` capped at 2; on resize the page restarts
   (debounced), because the pond is laid out for one size. Pools are preallocated (`ripples` is a fixed array of 80
   objects with an `alive` flag; nothing is pushed inside the loop).
3. **State that evolves over minutes**: koi have individual speeds, turning rates and schooling targets that drift;
   lily pads rotate and wander; the moon shimmer uses slow sine sums with incommensurate periods, so the pattern
   never repeats.
4. **`draw(dt)` in layers**: water gradient and caustics, pads, ripples (expanding, fading, recycled), koi (body as
   a chain of segments following the head, so turns look alive), moon glow last.
5. **The loop**: `dt` clamped to 0.05 s and multiplied by the reduced-motion factor, drawing skipped while hidden.
6. **A strong first frame**: koi are spawned already in a loose school near the centre, not off screen.

Reuse the shape, not the fish.
