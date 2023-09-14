import { TestBed } from '@angular/core/testing';

import { ItemsApi } from './items-api';

describe('ItemsApi', () => {
  let service: ItemsApi;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ItemsApi);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
