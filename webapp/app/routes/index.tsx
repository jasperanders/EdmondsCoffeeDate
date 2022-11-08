import { Form, Link, useActionData } from "@remix-run/react";
import { json } from "@remix-run/node"; // or cloudflare/deno
import { createNestedArrayFromString } from "~/helper/helper";


export const action = async ({ request }: any) => {
  const formData = await request.formData()
  const groupString = formData.get("groups")

  const groups = {
    groups: createNestedArrayFromString(groupString),
    number_dates: formData.get("datesNumber")
  }

  try {
    const url = process.env.MATCHING_URL ? process.env.MATCHING_URL : ""
    const response = await fetch(url,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(groups),
      }
    )
    console.log(response)

    return response
  } catch (e) { return e }
}

export default function Index() {

  const matches = useActionData()

  return (
    <main className="relative min-h-screen bg-white sm:flex sm:items-center sm:justify-center items-center">
      <div className="flex flex-col justify-center place-content-center">
        <>{console.log(matches)}</>
        <Form className="flex flex-col gap-4" method="post">
          <textarea name="groups" className="form-control
        w-full
        h-48
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        rounded
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"/>
          <input name="datesNumber" className="form-control
        block
        w-full
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300" type="number" />
          <input className="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
            type="submit" />
        </Form>
        {matches && <pre id="json">{JSON.stringify(matches.body.dates, null, 2)}</pre>}
      </div>
    </main>
  );
}
