__author__ = 'uddipaan'


def median(w):
    srt = sorted(w)
    print (srt)
    leng = len(srt)
    if not leng % 2:
        return int((srt[ leng // 2 ] + srt[ leng // 2 - 1]) // 2.0 )
    return int(srt[ leng // 2 ] )


