import sys

import geubsikpy

if __name__ == '__main__':
    sys.exit(
        geubsikpy.main(
            "run", sys.argv[-1]
        ),
    )
