export type Project = {
  _id: string;
  img: string;
  title: string;
  subtitle: string;
  description: string;
  button: {
    text: string;
    link: string;
  };
};

export type Post = {
  _id: string;
  img: string;
  title: string;
  caption: string;
  blocks: {
    title: string;
    text: string[];
  }[];
};
