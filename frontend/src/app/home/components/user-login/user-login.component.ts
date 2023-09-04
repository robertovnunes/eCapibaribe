import { Component, Input, OnInit } from '@angular/core';
import {
    FormControl,
    FormGroup,
    FormBuilder,
    Validators,
} from '@angular/forms';
import { Router } from '@angular/router';

function getUser(value: string | null) {
    if (value === 'admin') {
        return { username: 'admin', password: '123456' };
    } else {
        return { username: '', password: '' };
    }
}

@Component({
    selector: 'app-user-login',
    templateUrl: './user-login.component.html',
    styleUrls: ['./user-login.component.scss'],
})
export class UserLoginComponent implements OnInit {
    usernameInput!: HTMLInputElement | null;
    passwordInput!: HTMLInputElement | null;
    textError!: HTMLParagraphElement | null;

    username!: FormControl<string | null>;
    password: FormControl<string | null>;
    form: FormGroup;
    bcrypt = require('bcrypt');
    saltRounds = 10;
    hashedPassword!: string;

    constructor(private readonly fb: FormBuilder, private router: Router) {
        this.username = this.fb.control('', [Validators.required]);
        this.password = this.fb.control('', [Validators.required]);
        this.form = this.fb.nonNullable.group({
            username: this.username,
            password: this.password,
        });
    }

    ngOnInit() {
        this.usernameInput = document.querySelector('input[name="username"]');
        this.passwordInput = document.querySelector('input[name="password"]');
        this.textError = document.querySelector('.login-error-paragraph');
        this.hashedPassword = this.bcrypt
            .hash('123456', this.saltRounds)
            .then((hash: any) => {
                return hash;
            })
            .catch((err: any) => {
                console.log(err);
            });
    }

    countError = 0;

    loginError(mensagem: string) {
        this.usernameInput!.style.borderColor = 'red';
        this.passwordInput!.style.borderColor = 'red';
        this.textError!.textContent = mensagem;
        this.textError!.style.display = 'block';
        alert(mensagem);
        this.countError++;
        console.log(this.countError);
    }

    doLogin() {
        if (this.form.invalid) {
            this.loginError('Username or Password is empty');
            return false;
        }
        let result = false;
        const user = getUser(this.username.value);
        if (user.username === 'admin') {
            if (user.password === '123456') {
                result = true;
            } else {
                result = false;
            }
        }
        if (result) {
            alert('Login Successfull');
            this.router.navigateByUrl('/home', { replaceUrl: true });
            return true;
        } else {
            this.loginError('Username or Password is incorrect');
            alert('Login Failed');
            return false;
        }
    }
}
