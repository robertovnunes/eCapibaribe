import { Component, OnInit } from '@angular/core';
import { User } from '../../types/users/user';
import { TesteApi } from '../../api/register-api/register-api.component';

@Component({
    selector: 'app-cadastro',
    templateUrl: './cadastro.component.html',
    styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent implements OnInit {
    user: User;
    constructor(private testApi: TesteApi) { }
    
    ngOnInit(): void {
        this.user = new User();
        console.debug("entrei init")
    }
    
    
    onSubmit() {
        console.log(this.user);
        this.testApi.postRegister(this.user)
        // alert('Form Submitted succesfully!!!\n Check the values in browser console.');
        this.user = new User();
      }

    patternValidator(senha: string): boolean {
        const regex = new RegExp('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^a-zA-Z0-9\s]).{6,}$');
        const valid = regex.test(senha);
        return valid ? false : true;
    };

    patternValidatorEmail(email: string): boolean {
        const regex = new RegExp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');
        const valid = regex.test(email);
        return valid ? false : true;
    };
}
