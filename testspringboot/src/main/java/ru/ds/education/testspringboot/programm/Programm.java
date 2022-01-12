package ru.ds.education.testspringboot.programm;

import java.io.BufferedReader;

import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class Programm {
    public void start() {
        File file = new File("src/Core/main.py");

        try {
            Process process = Runtime.getRuntime().exec(new String[]{"python", file.getAbsolutePath()});
            BufferedReader br = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String s = br.readLine();
            System.out.println(s);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
