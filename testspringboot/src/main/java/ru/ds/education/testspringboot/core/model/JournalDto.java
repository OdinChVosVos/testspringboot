package ru.ds.education.testspringboot.core.model;

import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class JournalDto {

    @ApiModelProperty("id записи")
    private Long id;

    @ApiModelProperty("Количество выстрелов у польователя за вход")
    private int kolVis;

    @ApiModelProperty("Количество попаданий у пользователя за вход")
    private int popad;

    @ApiModelProperty("Информация о пользователе")
    private BdDto user;

}
