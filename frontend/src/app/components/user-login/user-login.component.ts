import {Component, Input, OnInit} from '@angular/core';
import {UserService} from '../../services/user.service';
import {User} from '../../models/user';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";

@Component({
    selector: 'app-user-login',
    templateUrl: './user-login.component.html',
    styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent implements OnInit {

    user: User[] = [];
    form!: FormGroup;
    formData = {
        username: '',
        password: ''
    };


    constructor(private userService: UserService, private formBuilder: FormBuilder) {

    }

    ngOnInit(): void {
        //this.criarForm();
    }

    doLogin() {
        console.log();
        this.userService.getUserByCPF(this.formData.username).subscribe((user: User[]) => {
            if (user.length != 0) {
                this.user = user;
                this.checkPassword(this.user);
            }});
        this.userService.getUserByEmail(this.formData.username).subscribe((user) => {
                if (user.length != 0) {
                    this.user = user;
                    this.checkPassword(this.user);
                }
                });
                if (this.user[0].cpf === this.formData.username || this.user[0].email === this.formData.username) {
                    console.log("quarto");
                    this.checkPassword(this.user);
                }
            }


    checkPassword(user: User[]):boolean {
        console.log("quinto");
        if (user[0].senha === this.formData.password) {
            console.log("sexto");
            alert('Login efetuado com sucesso!');
            return true;
        } else {
            console.log("setimo");
            alert('Senha incorreta!');
            return false;
        }
    }

}
