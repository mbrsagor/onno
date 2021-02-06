import Head from 'next/head';
import styles from './Layout.module.css';

const Layout = ({children, title="World Ranks"}) => {
    return (
        <div className={styles.container}>
        <Head>
            <title>{title}</title>
            <link rel="icon" href="/favicon.ico" />
        </Head>

        <main className={styles.main}>{children}</main>

        <footer className={styles.footer}>
            <p>&copy; 2021 All rights reserved. develop by <a href="https://mbrsagorbd.wordpress.com">Mbr Sagor</a>  </p>
        </footer>
    </div>
    )
}
export default Layout;
