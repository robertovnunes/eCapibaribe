import {Component, Input, OnInit} from '@angular/core';
import { Category } from "../../../service/interfaces/category";
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import {CategoriesService} from "../../../service/categories/categories.service";

@Component({
  selector: 'app-create-categories',
  templateUrl: './create-categories.component.html',
  styleUrls: ['./create-categories.component.css']
})
export class CreateCategoriesComponent implements OnInit{

  private category!: Category;
  catnameInput!: HTMLInputElement | null;
  catdescInput!: HTMLInputElement | null;
  catkeywordsInput!: HTMLInputElement | null;
  catimageInput!: HTMLInputElement | null;

  catname: FormControl<string | null>
  catdesc: FormControl<string | null>
  catkeywords: FormControl<string | null>
  catimage: FormControl<string | null>

  form: FormGroup;

  newCategory!: Category;


  constructor(private readonly fb: FormBuilder,
              private router: Router,
              private categoriesService: CategoriesService) {
    this.catname = this.fb.control('', [Validators.required]);
    this.catdesc = this.fb.control('', [Validators.required]);
    this.catkeywords = this.fb.control('', [Validators.required]);
    this.catimage = this.fb.control('', [Validators.required]);
    this.form = this.fb.nonNullable.group({
      catname: this.catname,
      catdesc: this.catdesc,
      catkeywords: this.catkeywords,
      catimage: this.catimage
    });
  }

  ngOnInit(): void {
    this.catnameInput = document.querySelector('input[name="name"]');
    this.catdescInput = document.querySelector('input[name="description"]');
    this.catkeywordsInput = document.querySelector('input[name="keywords"]');
    this.catimageInput = document.querySelector('input[name="image"]')
  }


  save() {
    if (this.form.invalid){
      alert("Ta faltando alguma coisa!");
      return false;
    }
    else {
      this.newCategory.name = this.catname.toString();
      this.newCategory.description = this.catdesc.toString();
      this.newCategory.keywords = this.catkeywords.toString();
      this.newCategory.image = this.catimage.toString();
      this.categoriesService.addCategory(this.newCategory);
      return true;
    }

  }
}
