'''
This program is used to experiment, test and try FFMPEG library in order to learn the basic concepts
Atakan Atamert, 2019
'''

import os

testFiles = ["KristenAndSara_720p.y4m", "720p5994_stockholm_ter.y4m"]

qpValuesToTest = [10, 20, 30, 40, 50 , 60, 70]

qpValuesToTestEncoding = [30, 40, 50]

gopLength = [1, 5, 10, 15, 30, 60, 100, 300, 600]

refValues = [1, 2, 4, 8, 16]

maxRange = [4, 8, 16]

bFrames = [0, 2, 4, 8]

psnrValues = []

ssimValues = []

print("--------------------------- TESTING DIFFERENT QP VALUES ---------------------------")

#Uncomment to test rate-distortion
'''
for testSubject in testFiles:
    for x in qpValuesToTestEncoding:
        currFilename = testSubject.replace('.y4m', '')
        curr = "ffmpeg -i " + testSubject + " -c:v libx264 -pix_fmt yuv420p -an -x264-params qp=" + str(x) + " " + currFilename + "_QP" + str(x) + ".mp4"
        curr2 = "ffmpeg -i " + testSubject + " -c:v libx265 -pix_fmt yuv420p -an -x265-params qp=" + str(x) + " " + currFilename + "_QP" + str(x) + ".mp4"
        curr3 = "ffmpeg -i " + testSubject + " -c:v libaom-av1 -pix_fmt yuv420p -strict experimental -an -qp " + str(x) + " " + currFilename + "_QP" + str(x) + ".mp4"

        psnr = "ffmpeg -i " + currFilename + "_QP" + str(x) + ".mp4 -i " + testSubject + ' -an -filter_complex "psnr" -f null - > tmp.txt 2>&1'

        #os.system(curr)

        if os.path.exists('null'):
            os.remove("null")
        os.system(psnr)

        strP = open('tmp.txt', 'r').read()

        for item in strP.split("\n"):
            if "PSNR" in item:
                psnrValues.append(str(item) + "   ------->   " + currFilename + "_QP" + str(x))

        os.remove('tmp.txt')

'''

#Uncomment for B-Frame test
'''
testSubject1 = "720p5994_stockholm_ter.y4m"
testSubject2 = "KristenAndSara_720p.y4m"
currFilename = testSubject2.replace('.y4m', '')
for b in bFrames:
    curr = "ffmpeg -i " + testSubject2 + " -c:v libx264 -pix_fmt yuv420p -an -qp 20 -g 250 -refs 2 -bf " + str(b) + " " + currFilename + "B" + str(b) + ".mp4"
    os.system(curr)
'''


#Uncomment for search algorithm test
'''
testSubject1 = "720p5994_stockholm_ter.y4m"
testSubject2 = "KristenAndSara_720p.y4m"
currFilename = testSubject1.replace('.y4m', '')
for ran in maxRange:
    curr = "ffmpeg -i " + testSubject1 + " -c:v libx264 -pix_fmt yuv420p -an -qp 20 -g 250 -refs 2 -me_method 2 -me_range " + str(ran) + " "+ currFilename + "RAN" + str(ran) + ".mp4"
    os.system(curr)
'''

#Uncomment for ref test
'''
testSubject1 = "720p5994_stockholm_ter.y4m"
testSubject2 = "KristenAndSara_720p.y4m"
currFilename = testSubject2.replace('.y4m', '')
for ref in refValues:
    curr = "ffmpeg -i " + testSubject2 + " -c:v libx264 -pix_fmt yuv420p -an -qp 20 -g 250 -refs " + str(ref) + " " + currFilename + str(ref) + "GOP250_QP20.mp4"
    os.system(curr)

'''


#Uncomment for GOP Test
'''
testSubject1 = "720p5994_stockholm_ter.y4m"
testSubject2 = "KristenAndSara_720p.y4m"
currFilename = testSubject2.replace('.y4m', '')
for gop in gopLength:
    curr = "ffmpeg -i " + testSubject2 + " -c:v libx264 -pix_fmt yuv420p -an -qp 20 -g " + str(gop) + " " + currFilename + str(gop) + "_QP20.mp4"
    os.system(curr)
'''



#Uncomment following to test with Noise.mp4
'''
for testSubject in testFiles:
    currFilename = testSubject.replace('.y4m', '')
    psnr = "ffmpeg -i Noise.mp4 -i " + testSubject + ' -an -filter_complex "psnr" -f null - > tmp.txt 2>&1'
    ssim = "ffmpeg -i Noise.mp4 -i " + testSubject + ' -an -filter_complex "ssim" -f null - > tmp1.txt 2>&1'
    if os.path.exists('null'):
        os.remove("null")
    os.system(psnr)

    strP = open('tmp.txt', 'r').read()

    for item in strP.split("\n"):
        if "PSNR" in item:
            psnrValues.append(str(item) + "   ------->   " + currFilename)
    # print("PSNR finished.")

    if os.path.exists('null'):
        os.remove("null")
    os.system(ssim)

    strS = open('tmp1.txt', 'r').read()

    for item in strS.split("\n"):
        if "SSIM" in item:
            ssimValues.append(str(item) + "   ------->   " + currFilename + "_QP")

    os.remove('tmp1.txt')
    os.remove('tmp.txt')
    # print("SSIM finished.")
'''

#Uncomment following to test with file encoding
'''
for testSubject in testFiles:
    for x in qpValuesToTest:
        currFilename = testSubject.replace('.y4m', '')
        curr = "ffmpeg -i " + testSubject + " -c:v libx264 -pix_fmt yuv420p -an -qp " + str(x) + " " + currFilename + "_QP" + str(x) + ".mp4"
        psnr = "ffmpeg -i " + currFilename + "_QP" + str(x) + ".mp4 -i " + testSubject + ' -an -filter_complex "psnr" -f null - > tmp.txt 2>&1'
        ssim = "ffmpeg -i " + currFilename + "_QP" + str(x) + ".mp4 -i " + testSubject + ' -an -filter_complex "ssim" -f null - > tmp1.txt 2>&1'

        os.system(curr)
        #print("QP " + str(x) + " for " + testSubject + " finished.")

        if os.path.exists('null'):
            os.remove("null")
        os.system(psnr)

        strP = open('tmp.txt', 'r').read()

        for item in strP.split("\n"):
            if "PSNR" in item:
                psnrValues.append(str(item) + "   ------->   " + currFilename + "_QP" + str(x))
        #print("PSNR finished.")

        if os.path.exists('null'):
            os.remove("null")
        os.system(ssim)

        strS = open('tmp1.txt', 'r').read()

        for item in strS.split("\n"):
            if "SSIM" in item:
                ssimValues.append(str(item) + "   ------->   " + currFilename + "_QP" + str(x))

        os.remove('tmp1.txt')
        os.remove('tmp.txt')
        #print("SSIM finished.")
'''

print("--------------------------- PSNR VALUES ---------------------------")
for psnrVal in psnrValues:
    print(psnrVal)

print("--------------------------- SSIM VALUES ---------------------------")
for ssimVal in ssimValues:
        print(ssimVal)

print("--------------------------- MP4 FILE SIZES ---------------------------")
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".mp4"):
        print("Size of " + filename + " is " + str(os.path.getsize(filename)))

print("--------------------------- FILE BITRATES ---------------------------")
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".mp4"):
        # 0.166667 is a fixed duration which corresponds to 10 seconds
        print("Bitrate of " + filename + " is " + str(os.path.getsize(filename)/0.166667))
