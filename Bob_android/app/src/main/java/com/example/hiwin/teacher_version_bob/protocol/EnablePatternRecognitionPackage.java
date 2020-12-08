package com.example.hiwin.teacher_version_bob.protocol;

public class EnablePatternRecognitionPackage extends Package {
    public EnablePatternRecognitionPackage(boolean functionEnabled) {
        super((byte)1,setData(functionEnabled));
    }

    private static byte[] setData(boolean enable){
        return new byte[]{(byte)(enable?1:0)};
    }

}
