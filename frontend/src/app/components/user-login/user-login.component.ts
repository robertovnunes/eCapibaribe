import {Component, Input, OnInit} from '@angular/core';
import {UserService} from '../../services/user.service';
import {User} from '../../models/user';


@Component({
    selector: 'app-user-login',
    templateUrl: './user-login.component.html',
    styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent implements OnInit {

    user: User[] = [];
    formData = {
        username: '',
        password: ''
    };


    constructor(private userService: UserService) {

    }

    ngOnInit(): void {
        //this.criarForm();
    }

    doLogin() {
        console.log();
        //this.user = this.getUser(this.formData.username);
        console.log(this.user);
    }

    getUser(username: string)/*: User[] */{
        let usuario!: User[];
        this.userService.getUserByCPF(this.formData.username).subscribe((user: User[]) => {
            if (user.length > 0) {
                console.log(user);
                //usuario = user;
            }
        });
        this.userService.getUserByEmail(this.formData.username).subscribe((user) => {
            if (user.length > 0) {
                console.log(user);
                //usuario = user;
            }
        });
        //console.log(usuario);
        //return usuario;
}

    checkPassword(user: User[]): boolean {
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
