package ru.ds.education.testspringboot.api.job;

import org.springframework.scheduling.annotation.Async;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;


@Component
public class MyTimerTask {

    @Scheduled(initialDelay = 2000, fixedRate = 3000)
    @Async
    public static void waiting() {
        System.out.println("veverdvb ");
    }
}