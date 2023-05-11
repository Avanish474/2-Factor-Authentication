package com.qrappcode.qrdemo;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;



public class LoginActivity extends AppCompatActivity {
    EditText email;
    EditText password;
    FirebaseAuth mAuth;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        email = findViewById(R.id.txtuser);
        password = findViewById(R.id.txtPwd);


        mAuth = FirebaseAuth.getInstance();


    }

    @RequiresApi(api = Build.VERSION_CODES.O)
    public void login(View view) {
        String em = email.getText().toString();
        String pswd = password.getText().toString();
        mAuth.signInWithEmailAndPassword(em, pswd)
                .addOnCompleteListener(this, task -> {
                    if (task.isSuccessful()) {


                        Intent intent = new Intent(LoginActivity.this, MainActivity.class);

                        startActivity(intent);


                    } else {
                        Toast.makeText(this, "Wrong email or password", Toast.LENGTH_SHORT).show();

                    }
                });

    }


}