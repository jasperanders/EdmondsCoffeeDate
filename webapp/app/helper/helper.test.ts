import { expect, describe, it } from "vitest";
import { createNestedArrayFromString } from "./helper";

// The two tests marked with concurrent will be run in parallel
describe("createNestedArrayFromString", () => {
  it("should split the string as expected", async () => {
    const testString = `Alice     
Bob Banson
Peter

    Jordan
Dan
Fred`;

    const expected = [
      ["Alice", "Bob Banson", "Peter"],
      ["Jordan", "Dan", "Fred"],
    ];
    expect(createNestedArrayFromString(testString)).toEqual(expected);
  });
});
