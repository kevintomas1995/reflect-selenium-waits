const checkColorBeforeClick = (elementClass) => {
  cy.get(elementClass)
    .children(".list")
    .children(".list-item")
    .should("have.css", "color", "rgb(0, 0, 0)");
};

const checkColorAfterClick = (elementClass) => {
  cy.get(elementClass)
    .children(".list")
    .children(".list-item")
    .should("have.css", "color", "rgb(255, 255, 255)");
};

describe("waiting for elements - test", () => {
  it("should visit", () => {
    cy.visit("http://localhost:3000/");
  });

  it("should render the instant element and color should change after clicking it", () => {
    cy.get(".instant").should("be.visible");

    checkColorBeforeClick(".instant");

    cy.get(".instant").click();

    checkColorAfterClick(".instant");
  });

  it("should render the miliseconds element and color should change after clicking it", () => {
    cy.get(".miliseconds").should("be.visible");

    checkColorBeforeClick(".miliseconds");

    cy.get(".miliseconds").click();

    checkColorAfterClick(".miliseconds");
  });

  it("should render the timeout element and color should change after clicking it", () => {
    cy.get(".timeout").should("be.visible");

    checkColorBeforeClick(".timeout");

    cy.get(".timeout").click();

    checkColorAfterClick(".timeout");
  });
});
