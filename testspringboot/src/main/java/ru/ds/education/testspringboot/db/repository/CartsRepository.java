package ru.ds.education.testspringboot.db.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.ds.education.testspringboot.db.entity.Carts;

@Repository
public interface CartsRepository extends JpaRepository<Carts, Long> {

}
