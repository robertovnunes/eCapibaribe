import {Component, Input, OnInit} from '@angular/core';
import { Category } from "../../../../service/interfaces/category";
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import {CategoriesService} from "../../../../service/categories/categories.service";

@Component({
  selector: 'app-create-categories',
  templateUrl: './create-categories.component.html',
  styleUrls: ['./create-categories.component.css']
})
export class CreateCategoriesComponent implements OnInit{

  nameInput!: HTMLInputElement | null;
  descInput!: HTMLInputElement | null;
  keywordsInput!: HTMLInputElement | null;

  name: FormControl<string | null>
  desc: FormControl<string | null>
  keywords: FormControl<string | null>
  image: FormControl<string | null>

  form: FormGroup;


  constructor(private readonly fb: FormBuilder,
              private router: Router,
              private categoriesService: CategoriesService) {
    this.name = this.fb.control('', [Validators.required]);
    this.desc = this.fb.control('', [Validators.required]);
    this.keywords = this.fb.control('', [Validators.required]);
    this.image = this.fb.control('', [Validators.required]);
    this.form = this.fb.nonNullable.group({
      name: this.name,
      desc: this.desc,
      keywords: this.keywords,
    });
  }

  ngOnInit(): void {
    this.nameInput = document.querySelector('input[name="name"]');
    this.descInput = document.querySelector('input[name="desc"]');
    this.keywordsInput = document.querySelector('input[name="keywords"]');
  }


  save() {

    let newCategory: Category;
    newCategory = {} as Category;
    if (!(this.name == null || this.desc == null || this.keywords == null)) {
      newCategory.name = <string>this.name.value;
      newCategory.description = <string>this.desc.value;
      newCategory.keywords = [<string>this.keywords.value];
      newCategory.items = [];
      this.categoriesService.addCategory(newCategory).subscribe(res => {
        if (res.status_code !== 201) {
            alert("Erro ao criar categoria! "+ res.message);
            return false;
      }
        alert("Categoria criada com sucesso!");
        this.router.navigate(['list-categories'], {replaceUrl: true}).then();
        return true;
      });
      return true;


    }
    return true;

  }

  cancel() {
    this.router.navigateByUrl('/categories', {replaceUrl: true}).then();
  }
}
