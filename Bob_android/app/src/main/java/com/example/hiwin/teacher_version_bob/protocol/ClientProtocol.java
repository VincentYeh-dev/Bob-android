package com.example.hiwin.teacher_version_bob.protocol;

import android.util.Log;

import com.example.hiwin.teacher_version_bob.communication.SerialService;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class ClientProtocol {
    private ProtocolListener listener;
    public ClientProtocol() {

    }

    public void attach(ProtocolListener listener) {
        this.listener=listener;
    }

    public void receive(byte[] newData,SerialService service) {

        Package.Type type = Package.Type.getPackageType(newData);
        switch (type) {
            case ServerHello:
                OnReceiveServerHello(newData);
                break;
            case Message:
                OnReceiveMessage(newData);
                break;
            default:

                break;
        }
    }
    private void OnReceiveMessage(byte[] data){
        MessagePackage messagePackage=new MessagePackage(data);
        listener.OnReceiveMessage(messagePackage.getMessage());
        Log.d("ProtocolLog","receive message:"+messagePackage.getMessage());
    }
    private void OnReceiveServerHello(byte[] data) {
        ServerHelloPackage sh=new ServerHelloPackage(data);
        ServerHelloPackage.StatusCode statusCode=sh.getStatusCode();
        Log.d("ProtocolLog",statusCode.toString());
        if(statusCode== ServerHelloPackage.StatusCode.ALLOW){
            listener.OnProtocolConnected();
        }else{
            listener.OnConnectionRejected(statusCode);
        }

    }

    public void connect(SerialService service){
        ClientHelloPackage clientHelloPackage = new ClientHelloPackage();
        byte[] data=clientHelloPackage.toBytes();
        try {
            service.write(data);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


}
