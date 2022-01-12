package ru.ds.education.testspringboot.exceptions;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;


@ControllerAdvice
public class AwesomeExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler(ThereIsNoSuchUserException.class)
    protected ResponseEntity<AwesomeException> handleThereIsNoSuchUserException() {
        return new ResponseEntity<>(new AwesomeException("There is no such entry"),
                HttpStatus.NOT_FOUND);
    }

    @ExceptionHandler(IHaveHimException.class)
    protected ResponseEntity<AwesomeException> handleIHaveHimException() {
        return new ResponseEntity<>(new AwesomeException("There is already user with this login"),
                HttpStatus.NOT_FOUND);
    }

    @ExceptionHandler(NoRemoveException.class)
    protected ResponseEntity<AwesomeException> handleNoRemoveException() {
        return new ResponseEntity<>(new AwesomeException("There is no users to remove"),
                HttpStatus.NOT_FOUND);
    }


    @ExceptionHandler(CanTEditHimException.class)
    protected ResponseEntity<AwesomeException> handleCanTEditHimException() {
        return new ResponseEntity<>(new AwesomeException("There is no user with this id/this login is owned, already"),
                HttpStatus.NOT_FOUND);
    }

    @Data
    @AllArgsConstructor
    private static class AwesomeException {
        private String message;
    }
}
