package ru.ds.education.testspringboot.db.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import javax.persistence.*;

@Getter
@Setter
@NoArgsConstructor
@Entity
@Table(name = "Users")
public class Users {

    @Id @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "users_generator")
    @SequenceGenerator(name = "users_generator", sequenceName = "users_seq", allocationSize = 1)
    private Long id;

    private String name;
    private String phone;
    private String mail;
    private boolean agreement;

    public Users(String name, String phone, String mail, boolean agreement) {
        this.name = name;
        this.phone = phone;
        this.mail = mail;
        this.agreement = agreement;
    }
}
