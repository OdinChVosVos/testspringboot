package ru.ds.education.testspringboot.db.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.util.Objects;

@Getter
@Setter
@NoArgsConstructor
@Entity
@Table(name = "bd")
public class Bd {

    @Id @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "bd_generator")
    @SequenceGenerator(name = "bd_generator", sequenceName = "bd_seq", allocationSize = 1)
    private Long id;

    private String login;
    private String password;
    private int achieves;
    private int points;
    private int status;

    public Bd(String login, String password, int achieves, int points, int status) {
        this.login = login;
        this.password = password;
        this.achieves = achieves;
        this.points = points;
        this.status = status;

    }


}
