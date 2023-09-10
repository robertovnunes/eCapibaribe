import { Component, OnInit } from '@angular/core';
import { User } from '../../types/users/user';
import { TesteApi } from '../../api/teste-api/teste-api.component';

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
        this.user = new User();
      }
}
