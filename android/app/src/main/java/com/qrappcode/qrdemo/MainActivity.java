package com.qrappcode.qrdemo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;

import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    Button scanbtn;
    static TextView scantext;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        scantext= findViewById(R.id.scantext);
        scanbtn= findViewById(R.id.scanbtn);

            scanbtn.setOnClickListener(view -> startActivity(new Intent(getApplicationContext(),scannerView.class)));
    }
}