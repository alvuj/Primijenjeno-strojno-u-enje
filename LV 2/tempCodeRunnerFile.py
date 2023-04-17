for i in range (0,h):
    for j in range(0,v):
        img2[i][j] *= 10
        if img2[i][j] > 1:
          img2[i][j] = 1