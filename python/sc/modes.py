"""
Small experiments in using Python to calculate scales and modes in music.
"""


def scale(start_note=0, scale_steps=None):
    """ Returns scale as a list of integers.

    The integers in the returned list are the notes of the scale,
    expressed as number of semitones from the initial note, so
    the first note is 0 for example.

    :param start_note: 0-based integer representing the start note for the scale. Default is 0.
    :param scale_steps: A list of integers representing the step sizes between successive notes in the scale.
                        If not provided, then the default will produce a major scale.

    Examples:
        >>> scale()
        [0, 2, 4, 5, 7, 9, 11, 12]

        >>> scale(start_note=2)
        [0, 1, 3, 5, 7, 8, 10, 12]

    """
    if scale_steps is None:
        # number of semitone steps between successive notes in major scale
        scale_steps = [2, 2, 1, 2, 2, 2, 1]

    mode_steps = rotate(scale_steps, start_note)

    note = 0
    notes = [note]
    for step in mode_steps:
        note += step
        notes.append(note)

    return notes


def rotate(l, n):
    """ Rotate list leftwards l by n positions.

    Example:
    >>> rotate([1, 2, 3, 4, 5, 6], 1)
    [2, 3, 4, 5, 6, 1]


    :param l: The list to be rotated.
    :param n: The integer number of positions to rotate. If larger than len(l) it will be reduced modulo len(l).
    """
    n %= len(l)
    return l[n:] + l[:n]


def steps(notes):
    """ Calculate intervals between successive notes.

    Example:
        >>> steps([0, 1, 3, 4, 6, 7, 9])
        [1, 2, 1, 2, 1, 2]

    """
    if len(notes) < 2:
        return []
    steps = [notes[i]-notes[i-1] for i in range(1, len(notes))]
    return steps


def render(notes):
    """ Make a picture of the notes.

    Example:
        >>> render(scale())
        'x x xx x x x'
    """
    scale_steps = steps(notes)
    output = ''
    for i in scale_steps:
        output += 'X' + ' '*(i-1)
    output += 'X'
    return output

if __name__ == '__main__':
    #
    # Demonstration
    #
    def demo(name, scale_notes):
        print(name, render(scale_notes), scale_notes)

    demo('        M7:', [0, 4, 7, 11])
    demo('        m7:', [0, 3, 7, 11])
    demo('       dim:', [0, 3, 6, 9, 12])
    demo('       aug:', [0, 4, 8, 12])
    demo('    Ionion:', scale())
    demo('    Dorian:', scale(1))
    demo('  Phrygian:', scale(3))
    demo('    Lydian:', scale(4))
    demo('Mixolydian:', scale(5))
    demo('   Aeolian:', scale(6))
    demo('   Locrian:', scale(7))

    demo('Whole Tone:', scale(scale_steps=[2, 2, 2, 2, 2, 2]))
