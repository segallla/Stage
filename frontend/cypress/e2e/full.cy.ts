describe('MVP flow', () => {
  it('loads', () => {
    cy.visit('/')
    cy.contains('Open Geo Copilot')
  })
})
