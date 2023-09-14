import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CategoriesManagerComponent } from './categories-manager.component';

describe('CategoriesManagerComponent', () => {
  let component: CategoriesManagerComponent;
  let fixture: ComponentFixture<CategoriesManagerComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CategoriesManagerComponent]
    });
    fixture = TestBed.createComponent(CategoriesManagerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
