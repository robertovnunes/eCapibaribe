import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

// TODO: fix this test

import { HomeApi } from './home.api';

describe('HomeApi', () => {
    let api: HomeApi;

    beforeEach(() => {
        TestBed.configureTestingModule({
            imports: [HttpClientTestingModule],
            providers: [HomeApi],
        });
        api = TestBed.inject(HomeApi);
    });

    it('should be created', () => {
        expect(api).toBeTruthy();
    });
});
