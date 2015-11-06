from PyQt5.QtGui import QFont, QFontMetricsF

from cadnano.gui.views.styles import *

# Path Sizing
VIRTUALHELIXHANDLEITEM_RADIUS = 30
VIRTUALHELIXHANDLEITEM_STROKE_WIDTH = 2
PATH_BASE_WIDTH = 20  # used to size bases (grid squares, handles, etc)
PATH_HELIX_HEIGHT = 2 * PATH_BASE_WIDTH  # staple + scaffold
PATH_HELIX_PADDING = 50 # gap between PathHelix objects in path view
PATH_GRID_STROKE_WIDTH = 0.5
SLICE_HANDLE_STROKE_WIDTH = 1
PATH_STRAND_STROKE_WIDTH = 3
PATH_STRAND_HIGHLIGHT_STROKE_WIDTH = 8
PATH_SELECTBOX_STROKE_WIDTH = 1.5
PCH_BORDER_PADDING = 1
PATH_BASE_HL_STROKE_WIDTH = 2  # PathTool highlight box
MINOR_GRID_STROKE_WIDTH = 0.5
MAJOR_GRID_STROKE_WIDTH = 0.5
OLIGO_LEN_BELOW_WHICH_HIGHLIGHT = 5
OLIGO_LEN_ABOVE_WHICH_HIGHLIGHT = 500

# Path Drawing
PATH_XOVER_LINE_SCALE_X = 0.035
PATH_XOVER_LINE_SCALE_Y = 0.035

# Path Colors
SCAFFOLD_BKG_FILL = '#e6e6e6'
ACTIVE_SLICE_HANDLE_FILL = '#80ffcc99'
ACTIVE_SLICE_HANDLE_STROKE = '#80cc6633'
MINOR_GRID_STROKE = '#999999'
MAJOR_GRID_STROKE = '#333333'
SCAF_STROKE = '#0066cc'
HANDLE_FILL = '#0066cc'
PXI_SCAF_STROKE = '#990066cc'
PXI_STAP_STROKE = '#99cc0000'
PXI_DISAB_STROKE = '#ffcccccc'
RED_STROKE = '#cc0000'
ERASE_FILL = '#3fcc0000'
FORCE_FILL = '#3f00ffff'
BREAK_FILL = '#ffcc0000'
COLORBOX_FILL = '#cc0000'
COLORBOX_STROKE = '#666666'
STAP_COLORS = ['#cc0000',
              '#f74308',
              '#f7931e',
              '#aaaa00',
              '#57bb00',
              '#007200',
              '#03b6a2',
              '#1700de',
              '#7300de',
              '#b8056c',
              '#333333',
              '#888888']
SCAF_COLORS = ['#0066cc']

DEFAULT_STAP_COLOR = "#888888"
DEFAULT_SCAF_COLOR = "#cc0000"

SELECTED_COLOR = '#ff3333'
SELECTED_ALPHA = 24
DEFAULT_ALPHA = 12


SELECTIONBOX_PEN_WIDTH = 2.5

# Loop/Insertion path details
INSERTWIDTH = 2
SKIPWIDTH = 2

# Add Sequence Tool
INVALID_DNA_COLOR = '#cc0000'
UNDERLINE_INVALID_DNA = True

#Z values
#bottom
ZACTIVESLICEHANDLE = 10
ZPATHHELIXGROUP = 20
ZPATHHELIX = 30
ZPATHSELECTION = 40

ZXOVERITEM = 90

ZPATHTOOL = 130
ZSTRANDITEM = 140
ZENDPOINTITEM = 150
ZINSERTHANDLE = 160
#top

# sequence stuff Font stuff
SEQUENCEFONT = None
SEQUENCEFONTH = 15
SEQUENCEFONTCHARWIDTH = 12
SEQUENCEFONTCHARHEIGHT = 12
SEQUENCEFONTEXTRAWIDTH = 3
SEQUENCETEXTXCENTERINGOFFSET = 0
def setFontMetrics():
    """ Application must be running before you mess
    too much with Fonts in Qt5
    """
    global SEQUENCEFONT
    global SEQUENCEFONTMETRICS
    global SEQUENCEFONTCHARWIDTH
    global SEQUENCEFONTCHARHEIGHT
    global SEQUENCEFONTEXTRAWIDTH
    global SEQUENCETEXTXCENTERINGOFFSET
    global SEQUENCETEXTYCENTERINGOFFSET
    SEQUENCEFONT = QFont("Monaco")
    if hasattr(QFont, 'Monospace'):
        SEQUENCEFONT.setStyleHint(QFont.Monospace)
    SEQUENCEFONT.setFixedPitch(True)
    SEQUENCEFONTH = int(PATH_BASE_WIDTH / 3.)
    SEQUENCEFONT.setPixelSize(SEQUENCEFONTH)
    SEQUENCEFONTMETRICS = QFontMetricsF(SEQUENCEFONT)
    SEQUENCEFONTCHARWIDTH = SEQUENCEFONTMETRICS.width("A")
    SEQUENCEFONTCHARHEIGHT = SEQUENCEFONTMETRICS.height()
    SEQUENCEFONTEXTRAWIDTH = PATH_BASE_WIDTH - SEQUENCEFONTCHARWIDTH
    SEQUENCEFONT.setLetterSpacing(QFont.AbsoluteSpacing,
                                 SEQUENCEFONTEXTRAWIDTH)
    SEQUENCETEXTXCENTERINGOFFSET = SEQUENCEFONTEXTRAWIDTH / 4.
    SEQUENCETEXTYCENTERINGOFFSET = PATH_BASE_WIDTH * 0.6
#end def

XOVER_LABEL_FONT = QFont(THE_FONT, THE_FONT_SIZE, QFont.Bold)
VIRTUALHELIXHANDLEITEM_FONT = QFont(THE_FONT, 3*THE_FONT_SIZE, QFont.Bold)
XOVER_LABEL_COLOR = QColor(0,0,0)