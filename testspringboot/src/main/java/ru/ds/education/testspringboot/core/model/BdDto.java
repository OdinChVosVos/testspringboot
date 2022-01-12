package ru.ds.education.testspringboot.core.model;

import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class BdDto {

    @ApiModelProperty("id пользователя")
    private Long id;

    @ApiModelProperty("Логин пользователя")
    private String login;

    @ApiModelProperty("Пароль пользователя")
    private String password;

    @ApiModelProperty("Достижения пользователя")
    private int achieves;

    @ApiModelProperty("Очки пользователя")
    private int points;

    @ApiModelProperty("Статус доступа пользователя")
    private int status;

}
