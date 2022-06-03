describe("spec.cy.js", () => {
  it("should visit and lists should be visible", () => {
    cy.visit("http://localhost:3000/");

    cy.get(".instant").should("be.visible");
    cy.get(".miliseconds").should("be.visible");
    cy.get(".timeout").should("be.visible");
  });
});
