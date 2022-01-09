import numpy as np
import random
import math
import imageio

def generateKey(n):
    d = np.random.randint(256, size = (int(n/2),int(n/2)))          #Arbitrary Matrix, should be saved as Key also
    I = np.identity(int(n/2))
    a = np.mod(-d,256)

    b = np.mod((23 * np.mod(I - a,256)),256)
    k = np.mod(np.power(23,127),256)
    c = np.mod((I + a),256)
    c = np.mod(c * k, 256)

    A1 = np.concatenate((a,b), axis = 1)
    A2 = np.concatenate((c,d), axis = 1)
    A = np.concatenate((A1,A2), axis = 0)
    return A

def encryptImageHill(A,img):
    Enc1 = (np.matmul(A,img[:,:,0])) % 256
    Enc2 = (np.matmul(A ,img[:,:,1] )) % 256
    Enc3 = (np.matmul(A,img[:,:,2])) % 256

    Enc1 = np.resize(Enc1,(Enc1.shape[0],Enc1.shape[1],1))
    Enc2 = np.resize(Enc2,(Enc2.shape[0],Enc2.shape[1],1))
    Enc3 = np.resize(Enc3,(Enc3.shape[0],Enc3.shape[1],1))
    Enc = np.concatenate((Enc1,Enc2,Enc3), axis = 2)
    imageio.imwrite('encrypted/Encrypted.png',Enc)

def decryptImageHill(url,A,Enc,l,w):
    # Enc = imageio.imread('drive/My Drive/Encrypted.png')   
    Dec1 = (np.matmul(A ,Enc[:,:,0] )) % 256
    Dec2 = (np.matmul(A,Enc[:,:,1] )) % 256
    Dec3 = (np.matmul(A ,Enc[:,:,2] )) % 256

    Dec1 = np.resize(Dec1,(Dec1.shape[0],Dec1.shape[1],1))
    Dec2 = np.resize(Dec2,(Dec2.shape[0],Dec2.shape[1],1))
    Dec3 = np.resize(Dec3,(Dec3.shape[0],Dec3.shape[1],1))

    Dec = np.concatenate((Dec1,Dec2,Dec3), axis = 2)
    Final = Dec[:l,:w,:] 
    imageio.imwrite(url,Final)