import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../../types/users/user';

@Injectable()

export class TesteApi {
    
    constructor(private http: HttpClient) { }

    public postRegister(user: User){
        this.http.post("/api/users/register", user).subscribe((response: any)=> {
            console.log(response)
            if(response.msg == "Cadastro realizado com sucesso"){
                alert("Cadastro realizado com sucesso")
            }
            if(response.msg == "email já cadastrado"){
                alert("Email já cadastrado")
            }
            if(response.msg == "cpf já cadastrado"){
                alert("CPF já cadastrado")
            }
            if(response.msg == "cpf inválido"){
                alert("CPF inválido")
            }
            
        });
    }
}
