// jshint esversion:6
/* jshint node: true */
/* global test */
/* global beforeAll */
/* global describe */
/* global expect */

const buttonClick = require("../ClickMe");
beforeAll(() => {
    document.body.innerHTML = "<p id='par'></p>";
});

describe("DOM tests", () => {
    test("Expects content to change", () => {
        buttonClick();
        expect(document.getElementById("par")
            .innerHTML).toEqual("You are going to Switzerland");
    });
});