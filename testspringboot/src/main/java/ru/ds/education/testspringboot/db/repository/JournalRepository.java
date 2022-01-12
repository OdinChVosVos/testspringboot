package ru.ds.education.testspringboot.db.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import ru.ds.education.testspringboot.db.entity.Journal;
import java.util.List;

@Repository
public interface JournalRepository extends JpaRepository<Journal, Long> {

    @Query(value = "Select en from Journal en where en.popad = :popad")
    List<Journal> findByPopad(@Param("popad") int popad);

}
