import styles from '../styles/Home.module.css';
import Layout from '../components/layout/Layout';
import SearchInput from '../components/Searchinput/Searchinput';

export default function Home({countries}) {
  console.log(countries);
  return <Layout>
    <div className={styles.counts}>Found {countries.length} Country</div>
    <SearchInput placeholder="Search filter by name" />
  </Layout>
}


export const getStaticProps = async () => {
  const res = await fetch("https://restcountries.eu/rest/v2/all");
  const countries = await res.json();
  return {
    props: {
      countries
    }
  }
}
