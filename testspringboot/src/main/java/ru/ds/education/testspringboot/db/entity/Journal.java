package ru.ds.education.testspringboot.db.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Getter
@Setter
@NoArgsConstructor
@Entity
@Table(name = "journal")
public class Journal {

    @Id @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "journal_generator")
    @SequenceGenerator(name = "journal_generator", sequenceName = "journal_seq", allocationSize = 1)
    private Long id;

    private int kolVis;
    private int popad;

    @ManyToOne(fetch = FetchType.LAZY, cascade = CascadeType.ALL)
    @JoinColumn(name = "user_id")
    private Bd user;


    public Journal(int kolVis, int popad, Bd user) {
        this.kolVis = kolVis;
        this.popad = popad;
        this.user = user;
    }

}
