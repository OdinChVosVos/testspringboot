package ru.ds.education.testspringboot.api.job;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Async;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;


@Slf4j
@Service
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
public class MyTimerTask {

//    @Scheduled(initialDelay = 2000, fixedRate = 3000)
//    @Async
//    public static void waiting() {
//        System.out.println("veverdvb ");
//    }
    private static final String CRON = "*/10 * * * * *";

    @Scheduled(cron = CRON)
    public void book() {
        System.out.println("wehfcge");
    }
}