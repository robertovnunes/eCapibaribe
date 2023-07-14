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
    @Input() username: string = '';
    @Input() password: string = '';
    form!: FormGroup;


    constructor(private userService: UserService, private formBuilder: FormBuilder) {


    }

    criarForm() {

        this.form = this.formBuilder.group({

            username: ['', [Validators.required]],
            senha: ['', [Validators.required]]

        })

    }


    ngOnInit(): void {
        this.criarForm();
    }

    doLogin() {
        if(this.form.invalid) return;
        let user = this.getUser();
    }

    getUser() {
        this.userService.getUserByUsename(this.username).subscribe((user: User[]) => {
            return user;
        });
    }


}
