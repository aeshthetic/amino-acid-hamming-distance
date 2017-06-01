elk = ['M', 'V', 'L', 'S', 'A', 'T', 'D', 'K', 'S', 'N', 'V', 'K', 'A', 'A', 'W', 'G', 'K', 'V', 'G', 'G', 'N', 'A', 'P', 'A', 'Y', 'G', 'A', 'E', 'A', 'L', 'E', 'R', 'M', 'F', 'L', 'S', 'F', 'P', 'T', 'T']
elk = ''.join(elk)
muskShrew = ['-', 'V', 'L', 'S', 'A', 'A', 'D', 'K', 'A', 'N', 'V', 'K', 'A', 'A', 'W', 'D', 'K', 'V', 'G', 'G', 'Q', 'A', 'A', 'N', 'Y', 'G', 'A', 'E', 'A', 'L', 'E', 'R', 'T', 'F', 'A', 'S', 'F', 'P', 'T', 'T']
muskShrew = ''.join(muskShrew)
bandedArma = ['-', 'V', 'L', 'S', 'A', 'A', 'D', 'K', 'T', 'H', 'V', 'K', 'A', 'F', 'W', 'G', 'K', 'V', 'G', 'G', 'H', 'A', 'E', 'F', 'G', 'A', 'A', 'E', 'F', 'G', 'A', 'E', 'A', 'L', 'E', 'R', 'M', 'F', 'A', 'S', 'F', 'P', 'P', 'T']
bandedArma = ''.join(bandedArma)
caribou = ['-', 'V', 'L', 'S', 'A', 'A', 'D', 'K', 'S', 'N', 'V', 'K', 'A', 'A', 'W', 'G', 'K', 'V', 'G', 'G', 'N', 'A', 'P', 'A', 'Y', 'G', 'A', 'E', 'A', 'L', 'E', 'R', 'M', 'F', 'L', 'S', 'F', 'P', 'T', 'T']
caribou = ''.join(caribou)

#It took me this long to realize that i didn't need to manually list characters...
bat = "MVLSPADKTNVKAAWDKVGG"


animals = {
    "elk" : ''.join(elk), #I had to make up for my sins earlier
    "muskShrew" : ''.join(muskShrew),
    "bandedArma" : ''.join(bandedArma),
    "caribou" : ''.join(caribou),
    "bat" : bat,
    "cow" : "MVLSAADKGNVKAAWGKVGGHAAEYGAEALERMFLSFPTT",
    "bigBat" : "-VLSAADKGNVKAAWDKVGGQAGEYGAEALERMFLSFPTT",
    "hamster" : "-VLSAKDKTNISEAWGKIGGHAGEYGAEALERMFFVYPTT",
    "mouse" : "MVLSGEDKSNIKAAWGKIGGHAGEYGAEALERMFFVYPTT",
    "pallidBat" : "MVLSPADKTNVKAAWDKVGG"
}
